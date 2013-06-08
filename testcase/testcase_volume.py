from se34euca.testcase.testcase_base import *

class testcase_volume(testcase_base):

    def create_volume(self):
	print "=== runTest: Create Volume ==="
	self.eucaUITester.base.test_ui_login()
	self.eucaUITester.volume.test_ui_create_volume()
	self.eucaUITester.base.test_ui_logout()

    def delete_volume(self):
	print "=== runTest: Delete Volume ==="
	self.eucaUITester.base.test_ui_login()
	self.eucaUITester.volume.test_ui_delete_volume()
	self.eucaUITester.base.test_ui_logout()

    def create_snapshot_from_volume(self):
	print "=== runTest: Create Snapshot From Volume ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.volume.test_ui_create_snapshot_from_volume()
        self.eucaUITester.base.test_ui_logout()

if __name__ == "__main__":
    unittest.main()



