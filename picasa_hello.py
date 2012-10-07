import gdata.photos.service
import gdata.media
import gdata.geo

email = 'apirakb@gmail.com'
username = 'apirakb'
password = 'Spid#rman'

path = '/'

gd_client = gdata.photos.service.PhotosService()
gd_client.email = email
gd_client.password = password
# gd_client.source = 'exampleCo-exampleApp-1'
gd_client.ProgrammaticLogin()

albums = gd_client.GetUserFeed(user=username)
for album in albums.entry:
  print 'title: %s, number of photos: %s' % (album.title.text,
      album.numphotos.text)

# first_album = albums.entry[20]
# print 'title: %s, number of photos: %s, id: %s' % (first_album.title.text,
# 	first_album.numphotos.text, first_album.gphoto_id.text) 
	 
# photos = gd_client.GetFeed(
#     '/data/feed/api/user/%s/albumid/%s?kind=photo' % (
#         "apirakb", first_album.gphoto_id.text))
# for photo in photos.entry:
#   print 'Photo title:', photo.title.text