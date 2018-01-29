a=0

for i in {0..9999}
do 
    ./lockpicksim < lock.in > tmp.out
    Val=`./lockpicksim < lock.in`
    ((a+=1))
    sed -i "s/$i/$a/g" lock.in
    if grep -q UMDCTF tmp.out; then
        echo "$a"  
    fi
done
