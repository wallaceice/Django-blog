var EndGame = false;
const player1 = "X";
const player2 = "O";
var winner = "";
var Game_turn = player1;

Game_Status();
Game_Play();
function Game_Status() {

	switch (Game_turn) {
		case player1:
			var play = document.querySelectorAll("header img")[0];
			play.setAttribute("src", "{% static 'game/img/X.png' %}");
			break;
		case player2:
			var play = document.querySelectorAll("header img")[0];
			play.setAttribute("src", "{% static 'game/img/O.png' %}");
			break;
		default:
			alert(Error);
			return;
	}
}

function Game_Play() {

	var Box_in_lines = document.getElementsByTagName("td");
	for (var i = 0; i < Box_in_lines.length; i++) {
		Box_in_lines[i].addEventListener("click", function () {
			if (this.getElementsByTagName("img").length === 0) {
				if (Game_turn === player1) {
					//this.getElementsByTagName("img").src = 'img/O.png';
					this.innerHTML = "<img src = {% static 'game/img/X.png' %} class = 'image'>";
					this.setAttribute("Atributo", player1);
					Game_turn = player2;
				} else
					if (Game_turn === player2) {
						this.innerHTML = "<img src = {% static 'game/img/O.png' %} class = 'image'>";
						this.setAttribute("Atributo", player2);
						Game_turn = player1;
					}
				Game_Status();
				Results();

			}
		})
	}
}
async function Results() {

	var ID = ["a1", "a2", "a3",
		"b1", "b2", "b3",
		"c1", "c2", "c3"];
	for (var i = 0; i < 9; i++) {
		ID[i] = document.getElementById(ID[i]).getAttribute("Atributo");
	}													  /*0 1 2
	3 4 5
	6 7 8*/
	if ((ID[0] == ID[3] && ID[0] == ID[6] && ID[0] != "") || (ID[0] == ID[1] && ID[0] == ID[2] && ID[0] != "") || (ID[0] == ID[4] && ID[0] == ID[8] && ID[0] != "")) {
		winner = ID[0];
		EndGame = true;
	} else {
		if ((ID[4] == ID[3] && ID[4] == ID[5] && ID[4] != "") || (ID[4] == ID[1] && ID[4] == ID[7] && ID[4] != "") || (ID[4] == ID[2] && ID[4] == ID[6] && ID[4] != "")) {
			winner = ID[4];
			EndGame = true;
		} else {
			if (((ID[8] == ID[7] && ID[8] == ID[6]) || (ID[8] == ID[2] && ID[8] == ID[5])) && ID[8] != "") {
				winner = ID[8];
				EndGame = true;
				/*0 1 2
				  3 4 5
				  6 7 8*/
			} else {
				if ((ID[0] != "" && ID[1] != "" && ID[2] != "" && ID[3] != "" && ID[4] != "" && ID[5] != "" && ID[6] != "" && ID[7] != "" && ID[8] != "" && winner == "")) {
					winner = "Velha";
					EndGame = true;
				}
			}
		}
	}

	if (EndGame == true) {
		End_Restart();
	}
}
async function End_Restart() {
	await Time_waiting(50);
	Game_End();
	location.href = location.href;
}
function Time_waiting(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}
function Game_End() {
	switch (winner) {
		case player1:
			alert(" Fim de Jogo!!\n O Player 1( X ) ganhou");
			break;
		case player2:
			alert(" Fim de Jogo!!\n O Player2( O ) ganhou");
			break;
		case "Velha":
			alert(" Fim de Jogo!\n A velha ganhou XD");
			break;
		case "":
			alert(" Fim de Jogo!\n O jogo foi interrompido de modo inesperado!\nPor favor Tente novamente!");
			break;
	}
}