from simplecv import *

color = Color()
img = Image('JeepGood.png')
img = img.invert()
img2 = Image('JeepGood.png')
img2 = img2.invert()
#img2 = img2.resize(img.width,img.height)

blobs = img.find_blobs()
blobs2 = img2.find_blobs()



confuse = []

# fs = blobs[0].get_shape_context()
# fs.draw()
# img.show()
# time.sleep(20)
i = 0
for b in blobs:
    for d in blobs2:
        metric =  b.get_match_metric(d)
        result = b.show_correspondence(d,'bottom')
        title = "Match Quality: " + str(metric)
        result.draw_text(title,20,20,color=Color.RED,fontsize=42)
        result.show()
        fname = "SanityCheckExample"+str(i)+".png"
        i = i+ 1
        result.save(fname)
        print "------------------------------"
        print metric
        confuse.append(metric)

print confuse

confuse = np.array(confuse)


print confuse.reshape(4,4)

time.sleep(10)
