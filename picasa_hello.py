import gdata.photos.service
import gdata.media
import gdata.geo
import os

email = 'apirakb@gmail.com'
username = 'apirakb'
password = 'Spid#rman'
path = '/Users/apirakb/Pictures/Events'

check = True

# Prepare Google data
gd_client = gdata.photos.service.PhotosService()
gd_client.email = email
gd_client.password = password
gd_client.ProgrammaticLogin()
albums = gd_client.GetUserFeed(user=username)

# Prepare Photo file
os.chdir(path)
directories = os.listdir(os.getcwd())
print 'total directories: %d' % len(directories)



for album in albums.entry:
  photo_path = path + "/" + album.title.text
  if os.path.isdir(photo_path) == True:
    os.chdir(photo_path)
    photos = os.listdir(os.getcwd())
    local_photos = len(photos) - 1
    if album.numphotos.text == str(local_photos):
      if not check:
        print 'Album name: %s, photos: %s' % (album.title.text,
          album.numphotos.text)
    else:
      print 'Album name: %s, photos: %s, local photos %d' % (album.title.text,
        album.numphotos.text, local_photos)
  else:
    if not check:
      print 'Album name: %s, photos: %s < Not local directory' % (album.title.text, album.numphotos.text)


# first_album = albums.entry[20]
# print 'title: %s, number of photos: %s, id: %s' % (first_album.title.text,
#   first_album.numphotos.text, first_album.gphoto_id.text) 
     
# photos = gd_client.GetFeed(
#     '/data/feed/api/user/%s/albumid/%s?kind=photo' % (
#         "apirakb", first_album.gphoto_id.text))
# for photo in photos.entry:
#   print 'Photo title:', photo.title.text

# for directory in directories:
#     photo_path = path + "/" + directory
#     if os.path.isdir(photo_path) == True:
#         os.chdir(photo_path)
#         photos = os.listdir(os.getcwd())
#         print 'Directory name: %s, photos: %d' % (directory, len(photos))

