export const get = (selection) => {
  const element = document.querySelector(selection)

  if (element) {
    return element
  }
}

export const getAll = (selection) => {
  const elements = [...document.querySelectorAll(selection)]

  if (elements) {
    return elements
  }
}
