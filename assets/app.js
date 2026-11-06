/* Rental Increase SF — table filter + sort + counts.
   Progressive enhancement only: every table is fully readable without JS. */
(function () {
  "use strict";

  function norm(s) {
    return (s || "").toLowerCase().replace(/\s+/g, " ").trim();
  }

  /* ---------- filtering ---------- */
  var inputs = document.querySelectorAll("input[data-filter]");
  Array.prototype.forEach.call(inputs, function (input) {
    var key = input.getAttribute("data-filter");
    var table = input.closest(".card, .table-scroll") &&
                input.closest(".card, .table-scroll").querySelector("table.data");
    if (!table) {
      // fall back: first data table after this toolbar
      var host = input.parentElement;
      while (host && !table) {
        table = host.querySelector ? host.querySelector("table.data") : null;
        host = host.nextElementSibling || (host.parentElement && host.parentElement.nextElementSibling);
        if (host && host.nodeType !== 1) { host = null; }
      }
    }
    if (!table) { return; }

    var tbody = table.querySelector("tbody");
    if (!tbody) { return; }
    var rows = Array.prototype.slice.call(tbody.querySelectorAll("tr"));
    var counter = document.querySelector('[data-count="' + key + '"]');

    function updateCount() {
      if (!counter) { return; }
      var vis = rows.filter(function (r) { return !r.classList.contains("hidden"); }).length;
      counter.textContent = vis + " of " + rows.length + " rows";
    }

    input.addEventListener("input", function () {
      var q = norm(input.value);
      rows.forEach(function (row) {
        if (!q) { row.classList.remove("hidden"); return; }
        var hit = norm(row.textContent).indexOf(q) !== -1;
        row.classList.toggle("hidden", !hit);
      });
      updateCount();
    });

    updateCount();
  });

  /* ---------- sorting ---------- */
  var tables = document.querySelectorAll("table.data");
  Array.prototype.forEach.call(tables, function (table) {
    var thead = table.querySelector("thead");
    if (!thead) { return; }
    var ths = thead.querySelectorAll("th");

    Array.prototype.forEach.call(ths, function (th, idx) {
      th.classList.add("sortable");
      th.setAttribute("tabindex", "0");
      th.setAttribute("role", "button");

      function doSort() {
        var tbody = table.querySelector("tbody");
        if (!tbody) { return; }
        var rows = Array.prototype.slice.call(tbody.querySelectorAll("tr"));
        var dir = th.getAttribute("data-dir") === "asc" ? "desc" : "asc";

        Array.prototype.forEach.call(ths, function (o) { o.removeAttribute("data-dir"); });
        th.setAttribute("data-dir", dir);

        function val(row) {
          var cell = row.children[idx];
          if (!cell) { return ""; }
          return cell.textContent.replace(/[$,%\s]/g, "").trim();
        }

        rows.sort(function (a, b) {
          var x = val(a), y = val(b);
          var nx = parseFloat(x), ny = parseFloat(y);
          var cmp;
          if (!isNaN(nx) && !isNaN(ny) && x !== "" && y !== "") {
            cmp = nx - ny;
          } else {
            cmp = x.localeCompare(y, undefined, { numeric: true, sensitivity: "base" });
          }
          return dir === "asc" ? cmp : -cmp;
        });

        rows.forEach(function (r) { tbody.appendChild(r); });
      }

      th.addEventListener("click", doSort);
      th.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); doSort(); }
      });
    });
  });

  /* ---------- mark current page in nav ---------- */
  var here = location.pathname.split("/").pop() || "index.html";
  Array.prototype.forEach.call(document.querySelectorAll(".nav a"), function (a) {
    var href = a.getAttribute("href");
    if (href === here) { a.setAttribute("aria-current", "page"); }
  });
})();
