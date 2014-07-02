$.get("/api/subscription/", function(data) {
    $("#subscription_status").html(data);
});
