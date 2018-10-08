function opens(obj){
for(var i = 1;i<=4;i++){
if(i == obj){document.getElementById("dis"+i).style.display="block"
}else
document.getElementById("dis"+i).style.display="none"
}
}

function exhibit(obj){
for(var i = 1;i<=4;i++){
if(obj == i){
if(document.getElementById("disp"+i).style.display=="block"){
	document.getElementById("disp"+i).style.display="none"
}else
	document.getElementById("disp"+i).style.display="block"
}
}
}
