public_thumbnails :
	python3 publicize_thumbs.py

jpgs.txt :
	ls *.JPG > jpgs.txt

clean :
	rm -f jpgs.txt
