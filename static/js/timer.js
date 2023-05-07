const axios = require('axios');

const timerDisplay = document.querySelector('.timer-display');
const title = document.querySelector('.title')
const tagSelect = document.getElementById('tags');
const startButton = document.querySelector('.start-button');
const durationInput = document.getElementById('duration');

let timeLeft = 5; // 50 minutes in seconds
let countdown;
let selectedTag = tagSelect.value;
let onBreak = false;

let currentPomo = 1
let totalPomo = durationInput.value
let currentBreak = 0
let totalBreak = 0

/*
Number of Sessions = durationInput.value
tag = tagSelect.value
start and end time, record time at beginning and at
*/


function startTimer() {
    if (durationInput.value === 0){
        alert('Pomodoros must be larger than 0')
    }
  selectedTag = tagSelect.value;
  if (onBreak){title.textContent = "BREAK #" + String(currentBreak)}
  else{title.textContent = "WORK # "+ String(currentPomo)}
  countdown = setInterval(() => {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    timerDisplay.textContent = `${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    timeLeft--;
    if (timeLeft < 0) {
      clearInterval(countdown);
      timerDisplay.textContent = '00:00';
      timerComplete();
    }
  }, 1000);
}

function timerComplete() { 
  // Do something when timer reaches 0
  console.log(currentPomo,durationInput.value)
  if (currentPomo == durationInput.value){
    title.textContent = "DONE!!!"
    // record to database()
    send_session()
    return
  }
  if (onBreak){
    currentPomo++;
    timeLeft = 3
    onBreak = false
    startTimer()
  }else{
    currentBreak++
    onBreak = true
    timeLeft = 1
    startTimer()
  }
}

tagSelect.addEventListener('change', () => {
  selectedTag = tagSelect.value;
});

startButton.addEventListener('click', startTimer);

function startPyTimer(){
    fetch('/start_timer', {
        method: 'POST'
      }).then(response => {
        console.log(response);
      });
}

function send_session(){
  console.log('sending session')
  axios.post('/api/add_session',{data})
  .then(response => {
    console.log(response.data.result);
  })
}

const postData = async (url = '', data = {}) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  return response.json();
}

const data = {
  time_start: new Date(),
  time_end: new Date(),
  tag: "math",
  pomodoro_count: 2
};

postData('/api/add_session', {data})
  .then(data => {
    console.log(data.result);
    // do something with the result
  });
