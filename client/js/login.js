import { get } from './getElement.js'
import setMessage from './setMessage.js'

// select elements
const form = get('.form')
const username = get('#username')
const password = get('#password')

// regex
const FirstCharIsNum = /^[0-9].*$/

const validateInputs = () => {
  // username
  if (username.value === '') {
    setMessage('username is required')
    username.focus()
  } else if (username.value.match(FirstCharIsNum)) {
    setMessage('username cannot start with a number')
    username.focus()
  } else if (username.value.length < 4) {
    setMessage('username cannot be less than 4 characters')
    username.focus()
  }
  // password
  else if (password.value === '') {
    setMessage('password is required')
    password.focus()
  } else if (password.value.length < 6) {
    setMessage('password must be greater than or equals to 6 characters')
    password.focus()
  } else {
    setMessage('login successful')
  }
}
form.addEventListener('submit', (e) => {
  e.preventDefault()
  validateInputs()
})
