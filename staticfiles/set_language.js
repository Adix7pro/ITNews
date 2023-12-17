document.addEventListener('DOMContentLoaded', function() {
    const languageSelector = document.getElementById('language-selector');

    if (languageSelector) {
        languageSelector.addEventListener('change', function() {
            const selectedLanguage = languageSelector.value;

            fetch('/set_language/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({ language: selectedLanguage }),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to set language');
                }
                location.reload();
            })
            .catch(error => {
                console.error(error);
            });
        });
    }

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
});