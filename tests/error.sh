if videocloud | grep -q 'Error: Missing option "--url".'; then
    echo "PASSED: No video ID provided"
else
    echo "FAILED: No video ID provided"
    exit 1
fi

if videocloud --url=www.youtube.com | grep -q "The specified video either doesn't exist or doesn't have captions enabled."; then
    echo "PASSED: Bad video ID provided"
else
    echo "FAILED: Bad video ID provided"
    exit 1
fi
