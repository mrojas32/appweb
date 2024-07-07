import { fetchWrapper } from "./fetchWrapper";
import { getToken } from "../../dataModel/Session";


export const apiWrapper = {
    get,
    patch,
    post,
    put,
    delete: _delete
};


function formatPath (apiPath) {
    if (apiPath[0] === '/')
        return `/api/${apiPath.slice(1)}`

    return `/api/${apiPath}`
}

function renderHeaders (body) {
    const sessionToken = getToken();
    var contentType;

    if (body instanceof FormData) contentType = 'multipart/form-data';
    else if (body instanceof URLSearchParams) contentType = 'application/x-www-form-urlencoded';
    else contentType = 'application/json'
    
    if (sessionToken) {
        return {
            Authorization: `Bearer ${sessionToken}`,
            'Content-Type': contentType
        };
    }
    else {
        return {
            'Content-Type': contentType
        }
    }
}

function get(apiPath, options={}) {
    return fetchWrapper.get(
        formatPath(apiPath),
        { 
            headers: renderHeaders(),
            ...options
        }
    );
}


function patch(apiPath, body, options={}) {
    return fetchWrapper.patch(
        formatPath(apiPath),
        body,
        {
            headers: renderHeaders(body),
            ...options
        }
    );
}

function put(apiPath, body, options={}) {
    return fetchWrapper.put(
        formatPath(apiPath),
        body,
        {
            headers: renderHeaders(body),
            ...options
        }
    );
}

function post(apiPath, body, options={}) {
    return fetchWrapper.post(
        formatPath(apiPath),
        body,
        {
            headers: renderHeaders(body),
            ...options
        }
    );
}

function _delete(apiPath, options={}) {
    return fetchWrapper.delete(
        formatPath(apiPath),
        {
            headers: renderHeaders(),
            ...options
        }
    );
}
