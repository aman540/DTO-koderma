let select = document.getElementById('inputGroupSelect02')

select.addEventListener('change', () => {
    console.log(select.value)

    let amount = document.getElementById('inputamt')

    amount.value = (select.value)

})


document.getElementById('form2').addEventListener('submit', (e) => {
    e.preventDefault();

    let options = [...document.getElementsByTagName('option')]

    options.forEach(option => {
        option.value = option.innerHTML
        console.log(option)
    })

    form2.submit()





})