function callPythonFunction() {
  fetch('/backend_event', {
    method: 'POST'
  }).then(response => {
    console.log(response);
  });
}
callPythonFunction();


const gotoTimer = () => window.location.href = 'timer';
const gotoStats = () => window.location.href = ' ';