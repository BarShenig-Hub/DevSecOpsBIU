# Syslog Analyzer Script
# Analyzes /var/log/syslog for IP addresses and error keywords

SYSLOG_FILE="/var/log/syslog"

# Severity levels (most severe first)
SEVERITY_LEVELS=("FATAL" "CRITICAL" "ERROR" "WARNING")

# Global arrays to store data
declare -A ip_count
declare -A ip_severity

# Function 1: Find all lines with IP addresses in syslog
Find_IP_in_Syslog() {
    echo "Finding IP addresses in syslog..."
    
    # Get all lines containing IP addresses
    ip_lines=$(grep -P '\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b' "$SYSLOG_FILE")
    
    echo "Found lines with IP addresses."
}

# Function 2: Detect error keywords in the IP lines
Detect_Errors() {
    echo "Detecting error keywords..."
    
    # Filter lines that contain error keywords
    error_lines=$(echo "$ip_lines" | grep -iE "FATAL|CRITICAL|ERROR|WARNING")
    
    echo "Detected error lines."
}

# Function 3: Collect data - count IPs and their severity levels
Collecting_Data() {
    echo "Collecting data..."
    
    # Process each error line
    while IFS= read -r line; do
        # Extract IP address from line
        ip=$(echo "$line" | grep -oP '\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b' | head -1)
        
        if [ -n "$ip" ]; then
            # Increment count for this IP
            if [ -z "${ip_count[$ip]}" ]; then
                ip_count[$ip]=0
            fi
            ip_count[$ip]=$((ip_count[$ip] + 1))
            
            # Determine highest severity level in this line
            for severity in "${SEVERITY_LEVELS[@]}"; do
                if echo "$line" | grep -iq "$severity"; then
                    # Store the most severe level for this IP
                    current_severity="${ip_severity[$ip]}"
                    
                    # If no severity yet, or this one is more severe, update it
                    if [ -z "$current_severity" ]; then
                        ip_severity[$ip]="$severity"
                        break
                    else
                        # Check if new severity is more severe (appears earlier in array)
                        for level in "${SEVERITY_LEVELS[@]}"; do
                            if [ "$level" = "$severity" ]; then
                                ip_severity[$ip]="$severity"
                                break 2
                            elif [ "$level" = "$current_severity" ]; then
                                break 2
                            fi
                        done
                    fi
                fi
            done
        fi
    done <<< "$error_lines"
    
    echo "Data collection complete."
}

# Function 4: Generate the report file
generate_Report() {
    echo "Generating report..."
    
    local timestamp=$(date +"%d-%b-%Y")
    local time_now=$(date +"%H:%M")
    local report_file="$HOME/report-${timestamp}.rep"
    
    # Start writing report
    {
        echo "*******************************************************************************"
        echo "Report created at $time_now"
        echo ""
        
        if [ ${#ip_count[@]} -eq 0 ]; then
            echo "No IP addresses found with error/warning keywords in syslog."
        else
            # Sort IPs by severity level, then by count
            # First, create a sortable list: severity_index count ip
            for ip in "${!ip_count[@]}"; do
                severity="${ip_severity[$ip]}"
                count="${ip_count[$ip]}"
                
                # Get severity index (0=FATAL, 1=CRITICAL, 2=ERROR, 3=WARNING)
                severity_index=999
                for i in "${!SEVERITY_LEVELS[@]}"; do
                    if [ "${SEVERITY_LEVELS[$i]}" = "$severity" ]; then
                        severity_index=$i
                        break
                    fi
                done
                
                echo "$severity_index $count $ip $severity"
            done | sort -n -k1,1 -k2,2rn | while read sev_idx count ip severity; do
                echo "$ip address appeared in $count lines."
                
                if [ $count -eq 1 ]; then
                    echo "keyword appeared: $severity"
                else
                    echo "keywords appeared: $severity"
                fi
                echo ""
            done
        fi
        
        echo "*******************************************************************************"
    } > "$report_file"
    
    echo "Report saved to: $report_file"
    echo ""
    echo "=== Report Content ==="
    cat "$report_file"
}

# Function 5: Main function - orchestrates everything
main() {
    echo "=== Syslog Analyzer ==="
    echo ""
    
    Find_IP_in_Syslog
    Detect_Errors
    Collecting_Data
    generate_Report
    
    echo ""
    echo "Analysis complete!"
}

# Run the script
main