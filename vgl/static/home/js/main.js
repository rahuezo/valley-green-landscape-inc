function displayServices(element) {
  $(element).text(job_names[counter]);

  counter += 1;
  if (counter >= job_names.length) {
    counter = 0;
  }
}
