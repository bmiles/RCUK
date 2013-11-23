function fix_dates(collection) {
  collection.find({updated: null}).forEach(function fix_update(doc) {
    doc.updated = doc.created;
    if ('addresses' in doc)
      doc.addresses.address[0].updated = doc.addresses.address[0].created;
    collection.save(doc);
  });
}
fix_dates(db.organisations);
fix_dates(db.persons);
fix_dates(db.projects);
