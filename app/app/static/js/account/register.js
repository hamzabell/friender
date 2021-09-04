function genRandomImage(){
    const randInt = getRandomNumber(70, 1);
    document.getElementById('avatar').value = `https://i.pravatar.cc/300?img=${randInt}`;
    document.getElementById('avatar_image').src = `https://i.pravatar.cc/300?img=${randInt}`;;
}  

function getRandomNumber(max, min){
    return Math.floor(Math.random() * (max - min + 1) + min)
}