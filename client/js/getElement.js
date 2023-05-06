export const get = (selection) => {
  const element = document.querySelector(selection)

  if (element) {
    return element
  }
  throw new Error(`your selection "${selection}" does not exist"`)
}

export const getAll = (selection) => {
  const elements = [...document.querySelectorAll(selection)]

  if (!elements[0]) {
    throw new Error(`your selections "${selection}" do not exist"`)
  } else {
    return Element
  }
}
