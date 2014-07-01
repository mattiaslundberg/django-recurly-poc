$("form").on("submit", function(evnt) {
    evnt.preventDefault();
    var form = this;

    recurly.token(form, function(err, token) {
        if (err) {
            console.debug(err);
        }
        else form.submit();
    });
});
