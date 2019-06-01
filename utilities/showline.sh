LINE=$1

for f in `find . -name "*.tex"`
do
	CONTENT=`sed -n $LINE'p' $f`
	echo $f "("$LINE"):" $CONTENT
done
