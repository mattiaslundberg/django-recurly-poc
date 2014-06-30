jsonapi = function(url, method, params, callback) {
    $.post(url, JSON.stringify({
        method: method,
        params: params,
        id: 1,
        jsonrpc: "2.0"
    }), callback, "json");
}
