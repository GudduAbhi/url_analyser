# url_analyzer

In order to make our build point to system-wide sqlite3 (& to rectify the common build problem),
we need to do the following (I'm on my ubuntu machine)
my user-home directory is /home/abhishek (equivalent to '~')

# 1. Create the corresponding directories in the required paths
$ cd /usr/local/opt
$ sudo mkdir sqlite sqlite/lib sqlite/include ; cd ../
$ sudo mkdir zlib zlib/lib zlib/include

# 2. Export the flags
$ export LDFLAGS="-L/usr/local/opt/sqlite/lib -L/usr/local/opt/zlib/lib"
$ export CPPFLAGS="-I/usr/local/opt/sqlite/include -I/usr/local/opt/zlib/include"

# 3. First remove python installation if you have one, else directly goto 4
$ rm -rf ~/.pyenv/versions/3.5.2

# 4. Install the required python version
pyenv install 3.5.2

# 5. Make this version global
pyenv global 3.5.2
