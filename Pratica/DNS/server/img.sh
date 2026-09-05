if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <image_name> <tag>"
    exit 1
fi
#sudo docker login -u meslin
sudo docker build -t meslin/$1:$2 .
sudo docker push meslin/$1:$2
sudo docker tag meslin/$1:$2 meslin/$1:latest
sudo docker push meslin/$1:latest