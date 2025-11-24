let darkmode = localStorage.getItem('darkmode')
const theme = document.querySelector('#switch-mode')

theme.addEventListener("click", () => {
    darkmode = localStorage.getItem('darkmode')
    darkmode != 'active' ? enabledarkmode() : disableDarkmode();
})

const enabledarkmode = () => {
    document.body.classList.add('dark-mode')
    localStorage.setItem('darkmode', 'active')
}

const disableDarkmode = () => {
    document.body.classList.remove('dark-mode')
    localStorage.removeItem('darkmode')
}

if(darkmode === 'active') enabledarkmode()