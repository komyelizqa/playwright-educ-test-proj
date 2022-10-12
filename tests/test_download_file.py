class TestDownloadFile:

    def test_download_txt(self, download_file):
        download_file.navigate_to("File Download")
        download_file.check_text_exist("File Downloader")
        download_file.save_file("some-file.txt")
        assert download_file.check_file_exist_os("some-file.txt")

    def test_download_docx(self, download_file):
        download_file.navigate_to("File Download")
        download_file.save_file("test_doc.docx")
        assert download_file.check_file_exist_os("test_doc.docx")

    def test_download_png(self, download_file):
        download_file.navigate_to("File Download")
        download_file.save_file("Screenshot_1.png")
        assert download_file.check_file_exist_os("Screenshot_1.png")


