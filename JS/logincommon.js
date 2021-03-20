function emailValidate(emailSelector,errorSelector,validity)
{
    let emailInput=document.querySelector(emailSelector);
    let emailError = document.querySelector(errorSelector);
    emailInput.addEventListener('keyup', (e) => {
        
        if (emailInput.validity.typeMismatch) {
            emailError.style.color = 'red';
            emailInput.style.borderColor = 'red';
            emailInput.style.backgroundColor = '#ffb3b9'
            emailError.textContent = 'Enter a valid email!';
            validity = false;
        }
        else if(emailInput.value==='')
        {
            emailInput.style.borderColor='';
            emailInput.style.backgroundColor=''
            emailError.textContent='';
        }
        else {
            emailError.textContent = '';
            emailInput.style.borderColor = 'green';
            emailInput.style.backgroundColor = ''
            validity = true;
            return validity;
        }
    })
    return validity ;
} 

