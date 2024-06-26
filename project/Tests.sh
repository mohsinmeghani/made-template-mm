# Removing Existing Files
echo "Starting Tests"
echo "------------------------"

echo "running system test."
python ./system-test.py

# Check the return value of system_test.sh
if [ $? -ne 0 ]; then
    echo "System Test failed."
    exit 1
fi
