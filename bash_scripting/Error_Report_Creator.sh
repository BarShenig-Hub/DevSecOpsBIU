# Save all syslog lines that contain an IP address
grep -E '([0-9]{1,3}\.){3}[0-9]{1,3}(:[0-9]{1,5})?' /var/log/syslog > IPLines.txt
}

Detect_Errors() {

    # Clear old results to avoid appending duplicates
    > ErrorLines.txt

    while IFS= read -r line; do
        echo "$line" | grep -Ei 'error|failed' >> ErrorLines.txt
    done < IPLines.txt 

}

Collecting_Data() {
    # Count total errors 
    TotalErrors=$(wc -l < ErrorLines.txt)
    Date=$(date +"%d-%b-%Y")
} 

Print_Report() {
    > Report-$Date.rep
    printf "Total Errors in Syslog File are %s logs\n" "$TotalErrors" >> Report-$Date.rep
}

Find_IP_in_Syslog
Detect_Errors
Collecting_Data
Print_Report
