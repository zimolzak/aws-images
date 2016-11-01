index.html : jpgs.txt
	python3 make_index.py > index.html

thumbnails_public : jpgs.txt
	python3 publicize_thumbs.py

jpgs.txt :
	ls *.JPG > jpgs.txt

clean :
	rm -f index.html

deep_clean :
	rm -f jpgs.txt
