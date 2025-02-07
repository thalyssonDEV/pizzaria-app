document.getElementById("telefone").addEventListener("input", function (e) {
    this.value = this.value.replace(/\D/g, ""); // Remove tudo que não for número

    let v = e.target.value.replace(/\D/g, "");
    if (v.length > 10) {
        e.target.value = `(${v.slice(0, 2)}) ${v.slice(2, 7)}-${v.slice(7, 11)}`;
    } else if (v.length > 6) {
        e.target.value = `(${v.slice(0, 2)}) ${v.slice(2, 6)}-${v.slice(6)}`;
    } else if (v.length > 2) {
        e.target.value = `(${v.slice(0, 2)}) ${v.slice(2)}`;
    } else if (v.length > 0) {
        e.target.value = `(${v}`;
    }
});