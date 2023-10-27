// 코드를 작성해 주세요
const options = ["rock", "paper", "scissors"];
let playerSelection = null;
let computerSelection = null;
let isAnimating = false;

function updateDisplay(player, computer) {
    const gameElement = document.querySelector(".game");
    gameElement.innerHTML = `<h1>${player || "가위 바위 보"}</h1>
                            <p>${computer || ""}</p>`;
}

function computerPlay() {
    if (!isAnimating) {
        isAnimating = true;
        let count = 0;
        const animationInterval = setInterval(() => {
            count++;
            computerSelection = options[count % 3];
            updateDisplay(playerSelection, computerSelection);
            if (count === 30) {
                clearInterval(animationInterval);
                isAnimating = false;
                const result = playRound(playerSelection, computerSelection);
                resultText.textContent = result;
                resultModal.style.display = "flex";
            }
        }, 100);
    }
}

function playRound(playerSelection, computerSelection) {
    if (playerSelection === computerSelection) {
        return "비겼습니다!";
    } else if (
        (playerSelection === "rock" && computerSelection === "scissors") ||
        (playerSelection === "scissors" && computerSelection === "paper") ||
        (playerSelection === "paper" && computerSelection === "rock")
    ) {
        return "플레이어가 이겼습니다!";
    } else {
        return "컴퓨터가 이겼습니다!";
    }
}

const buttons = document.querySelectorAll(".options button");
const resultModal = document.getElementById("resultModal");
const resultText = document.getElementById("resultText");
const closeModal = document.getElementById("closeModal");

buttons.forEach((button) => {
    button.addEventListener("click", () => {
        if (!isAnimating) {
            playerSelection = button.id;
            computerPlay();
        }
    });
});

closeModal.addEventListener("click", () => {
    resultModal.style.display = "none";
});
