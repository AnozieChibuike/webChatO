// Regex
import { get } from './getElement.js'

const emailRegex = /^\w+([\\.-]?\w+)*@\w+([\\.-]?\w+)*(\.\w{2,3})+$/
const FirstCharIsNum = /^[0-9].*$/

// DOM Elements
const form = get('.form')
const message = get('.message')

const setMessage = (text) => {
  message.textContent = text
  message.classList.add('active')
  setTimeout(() => {
    message.textContent = ''
    message.classList.remove('active')
  }, 2000)
}

const validateInputs = () => {
  // select inputs
  const username = get('#username')
  const email = get('#email')
  const password = get('#password')
  const confirmPassword = get('#confirmPassword')

  if (confirmPassword) {
    if (confirmPassword.value !== password.value) {
      setMessage('passwords does not match, confirm password')
    }
  }
  if (password) {
    if (password.value === '') {
      setMessage('password is required')
    } else if (password.value.length < 6) {
      setMessage('password must be greater than or equals to 6 characters')
    }
  }
  if (username) {
    if (username.value === '') {
      setMessage('username is required')
    } else if (username.value.match(FirstCharIsNum)) {
      setMessage('username cannot start with a number')
    } else if (username.value.length < 4) {
      setMessage('username cannot be less than 4 characters')
    }
  }
  if (email) {
    if (email.value === '') {
      setMessage('email is required')
    } else if (!email.value.match(emailRegex)) {
      setMessage('invalid email')
    }
  }
}

form.addEventListener('submit', (e) => {
  e.preventDefault()
  validateInputs()
})
