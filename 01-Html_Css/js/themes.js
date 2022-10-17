function scroll_code (code_id) {
    if (code_id === 0) {
        document.querySelector("#tt1 .code").scrollTop += 100;
        document.querySelector("#tt1 .code").classList.add("scrolled")
}
}