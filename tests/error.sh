if ./videocloud | grep -q "Please specify a YouTube video link or video ID"; then
    echo "PASSED: No video ID provided"
else
    echo "FAILED: No video ID provided"
    exit 1
fi
