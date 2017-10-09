TEST_DIR=./test_dir
mkdir $TEST_DIR
echo "this is my test test" > $TEST_DIR/test1.txt
touch $TEST_DIR/test2.txt
mkdir -p $TEST_DIR/lv2/lv3
echo "this is not my test test" > $TEST_DIR/lv2/lv3/test3.txt
