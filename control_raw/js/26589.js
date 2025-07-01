function addClass(node, name) {
        if (hasClass(node, name)) {
            return;
        }
        if (node.classList) {
            node.classList.add(name);
        } else {
            node.className += " " + name;
        }
    }