const session = {
    token: null
    //token: '123'
};

const loadedToken = window.localStorage.getItem('session-token');
if (loadedToken) session.token = loadedToken;

export const setToken = (value) => {
    session.token = value;

    const newTokenEvt = new CustomEvent('session-token-update', {
        detail: {token: value}
    });
    document.dispatchEvent(newTokenEvt);

    window.localStorage.setItem('session-token', value);
};

export const getToken = () => session.token;

export const resetSession = () => {
    session.token = null;
    const newTokenEvt = new CustomEvent('session-token-update', {
        detail: {token: null}
    });
    document.dispatchEvent(newTokenEvt);

    window.localStorage.removeItem('session-token');
};
