// PRODUCT SEARCH — client-side filter over productData and industryData
(function () {
  var searchInput = document.getElementById('siteSearchInput');
  var searchResults = document.getElementById('searchResults');
  if (!searchInput || !searchResults) return;

  var MIN_CHARS = 2;
  var debounceTimer;

  function search(query) {
    var q = query.toLowerCase().trim();
    if (q.length < MIN_CHARS) { searchResults.innerHTML = ''; searchResults.classList.remove('open'); return; }

    var results = [];

    // Search products
    if (typeof productData !== 'undefined') {
      productData.forEach(function (p, i) {
        var score = 0;
        if (p.title && p.title.toLowerCase().indexOf(q) !== -1) score += 10;
        if (p.desc && p.desc.toLowerCase().indexOf(q) !== -1) score += 5;
        if (p.category && p.category.toLowerCase().indexOf(q) !== -1) score += 3;
        if (p.brands && p.brands.some(function (b) { return b.toLowerCase().indexOf(q) !== -1; })) score += 8;
        if (p.specs && p.specs.some(function (s) { return s.toLowerCase().indexOf(q) !== -1; })) score += 4;
        if (score > 0) results.push({ type: 'product', index: i, title: p.title, desc: p.desc, score: score });
      });
    }

    // Search industries
    if (typeof industryData !== 'undefined') {
      industryData.forEach(function (ind, i) {
        var score = 0;
        if (ind.title && ind.title.toLowerCase().indexOf(q) !== -1) score += 8;
        if (ind.desc && ind.desc.toLowerCase().indexOf(q) !== -1) score += 4;
        if (ind.items && ind.items.some(function (it) { return it.toLowerCase().indexOf(q) !== -1; })) score += 3;
        if (score > 0) results.push({ type: 'industry', index: i, title: ind.title, desc: ind.desc, score: score });
      });
    }

    // Search articles
    if (typeof articles !== 'undefined') {
      Object.keys(articles).forEach(function (key) {
        var a = articles[key];
        var score = 0;
        if (a.title && a.title.toLowerCase().indexOf(q) !== -1) score += 8;
        if (a.cat && a.cat.toLowerCase().indexOf(q) !== -1) score += 4;
        if (a.content && a.content.toLowerCase().indexOf(q) !== -1) score += 2;
        if (score > 0) results.push({ type: 'article', key: key, title: a.title, desc: a.cat, score: score });
      });
    }

    // Sort by score descending, limit to 8
    results.sort(function (a, b) { return b.score - a.score; });
    results = results.slice(0, 8);

    if (results.length === 0) {
      searchResults.innerHTML = '<div class="search-result-empty">No results found for "' + query + '"</div>';
    } else {
      var html = '';
      results.forEach(function (r) {
        html += '<div class="search-result-item" data-type="' + r.type + '" data-index="' + (r.index !== undefined ? r.index : '') + '" data-key="' + (r.key || '') + '">'
          + '<div class="search-result-type">' + (r.type === 'product' ? 'PRODUCT' : r.type === 'industry' ? 'INDUSTRY' : 'ARTICLE') + '</div>'
          + '<div class="search-result-title">' + highlightMatch(r.title, q) + '</div>'
          + '<div class="search-result-desc">' + (r.desc || '').substring(0, 80) + '</div>'
          + '</div>';
      });
      searchResults.innerHTML = html;

      // Click handlers
      searchResults.querySelectorAll('.search-result-item').forEach(function (el) {
        el.addEventListener('click', function () {
          var type = this.dataset.type;
          if (type === 'product') {
            if (typeof openProductDetail === 'function') openProductDetail(parseInt(this.dataset.index));
            searchInput.value = '';
            searchResults.innerHTML = '';
            searchResults.classList.remove('open');
          } else if (type === 'industry') {
            if (typeof openIndustryModal === 'function') openIndustryModal(parseInt(this.dataset.index));
            searchInput.value = '';
            searchResults.innerHTML = '';
            searchResults.classList.remove('open');
          } else if (type === 'article') {
            if (typeof openArticle === 'function') openArticle(this.dataset.key);
            searchInput.value = '';
            searchResults.innerHTML = '';
            searchResults.classList.remove('open');
          }
        });
      });
    }
    searchResults.classList.add('open');
  }

  function highlightMatch(text, query) {
    if (!text) return '';
    var idx = text.toLowerCase().indexOf(query.toLowerCase());
    if (idx === -1) return text;
    return text.substring(0, idx) + '<mark>' + text.substring(idx, idx + query.length) + '</mark>' + text.substring(idx + query.length);
  }

  searchInput.addEventListener('input', function () {
    clearTimeout(debounceTimer);
    var self = this;
    debounceTimer = setTimeout(function () { search(self.value); }, 200);
  });

  searchInput.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      searchInput.value = '';
      searchResults.innerHTML = '';
      searchResults.classList.remove('open');
      searchInput.blur();
    }
  });

  // Close on outside click
  document.addEventListener('click', function (e) {
    if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
      searchResults.classList.remove('open');
    }
  });

  // Focus handler to re-show results if query exists
  searchInput.addEventListener('focus', function () {
    if (this.value.trim().length >= MIN_CHARS) search(this.value);
  });
})();
