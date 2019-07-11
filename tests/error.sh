if videocloud | grep -q 'Error: Missing option "--url".'; then
    echo "PASSED: No video ID provided"
else
    echo "FAILED: No video ID provided"
    exit 1
fi
