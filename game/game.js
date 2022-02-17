let win = false
function ask(){
    if (win==false){
        guess = prompt("Enter your guess")
    }
}
for (i in Range(0,guess.length())){
    if (guess[i] == word[i]){
        shown_word[i] = "[!?]"
        document.getElementById("row1").innerHTML = shown_word
    }
}