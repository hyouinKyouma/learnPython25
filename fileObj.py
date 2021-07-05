# reading,wrting files in python
#basic syntax

with open('test.txt', 'r') as f:
    print(f.read()) 
    # f.close()

# dealing with image and other files by reading in byte mode 
with open('Morpheus.png', 'rb') as rf:
    with open('morpheus_copy.png','wb') as wf:
        chunksize = 1024
        rf_chunk = rf.read(chunksize)
        while len(rf_chunk) > 0:
            print("read chunk")
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunksize)
        # wf.close()
        # rf.close()            

            