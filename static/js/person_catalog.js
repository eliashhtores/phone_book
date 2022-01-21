const name = document.querySelector('#name')
const person_list = document.querySelector('#person_list')

const getPersonList = () => {
    http.get(`${server}/person/search?name=${name.value}`)
        .then((response) => {
            person_list.innerHTML = ''
            for (const element of response) {
                person_list.innerHTML += `<p><a href="#">${element.name}</a></p>`
            }
        })
        .catch((err) => {
            console.error(err)
        })
}

const localListeners = () => {
    name.addEventListener('input', getPersonList)
}

localListeners()
getPersonList()
