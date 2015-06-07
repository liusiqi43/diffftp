# Files should be organized like:
# ftp://ftp.com/BASE_FOLDER/Path/To/Folder1
# ftp://ftp.com/BASE_FOLDER/Another/Path/To/Folder2

FTP_URL = 'ftp.com'
BASE = 'BASE_FOLDER'

# Set to None if authentication not required
LOGIN = 'login'
# Set to None if authentication not required
PASSWD = 'passwd'

# files are downloaded to downloads/file1...
DOWNLOAD = 'downloads'

# Folders being monitered.
# The script will monitor 'ftp.com/BASE_FOLDER/Path/To/Folder1'
FOLDERS = ['Path/To/Folder1',
           'Another/Path/To/Folder2']
