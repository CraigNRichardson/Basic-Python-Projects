# Parent Class Fine Art
class FineArt:
    artist = ' '
    title = ' '
    date = ' '
    collection = ' '
    location = ' '

    def getInfo(self):
        print("\nArtist: {}\nTitle: {}\nDate Created: {}\nCollection: {}\nLocation: {}".format(self.artist,self.title,self.date,self.collection,self.location))
    
# Child Class Painting    
class Painting(FineArt):
    medium = ' '
    surface = ' '

    def getInfo(self):
        print("\nArtist: {}\nTitle: {}\nDate Created: {}\nCollection: {}\nLocation: {}\nMedium: {} on {}".format(self.artist,self.title,self.date,self.collection,self.location,self.medium,self.surface))

# Child Class Photography    
class Photography(FineArt):
    image_acquisition_method = ' '
    print_type = ' '

    def getInfo(self):
        print("\nArtist: {}\nTitle: {}\nDate Created: {}\nCollection: {}\nLocation: {}\nImage Acquisition Method: {}\nPrint Type: {}".format(self.artist,self.title,self.date,self.collection,self.location,self.image_acquisition_method,self.print_type))

if __name__ == "__main__":

    art = FineArt()
    art.getInfo()

    painting = Painting()
    painting.getInfo()

    photo = Photography()
    photo.getInfo()

    
    
