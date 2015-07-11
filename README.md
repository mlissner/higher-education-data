# Overview

There are a lot of good data sets about schools of higher education. Alas, all 
of them come in the form of spreadsheets. This little chunk of code takes those 
datasets and converts them to a `json` file that can be imported by 
freelawproject/courtlistener using the following Django model:

    class School(models.Model):
        is_alias_of = models.ForeignKey(
            'self',
            blank=True,
            null=True,
        )
        name = models.CharField(
            max_length=120,  # Dept. Ed. bulk data had a max of 91.
            db_index=True,
        )
        unit_id = models.IntegerField(
            help_text="This is the ID assigned by the Department of Education, as "
                      "found in the data on their API.",
            unique=True,
            db_index=True,
        )
        ein = models.IntegerField(
            help_text="The EIN assigned by the IRS",
            null=True,
            blank=True,
            unique=True,
            db_index=True,
        )
        ope_id = models.IntegerField(
            help_text="This is the ID assigned by the Department of Education's "
                      "Office of Postsecondary Education (OPE) for schools that "
                      "have a Program Participation Agreement making them eligible "
                      "for aid from the Federal Student Financial Assistance "
                      "Program",
            null=True,
            blank=True,
            unique=True,
            db_index=True,
        )
        
The final file, therefore, looks something like:

    [
      {
        "pk": 1,
        "model": "judges.School",
        "fields": [
          "is_alias_of": null,
          "name": "University of California Berkeley",
          "unit_id": ,
          "ein": ,
          "ope_id": ,
        ]
      },
      {
        "pk": 2,
        "model": "judges.School",
        "fields": [
          "is_alias_of": 1,
          "name": "Cal",
          "unit_id": null,
          "ein": null,
          "ope_id": null,
        ]
      }
    ]


# Limitations

1. This is only data for U.S. universities.


# Sources

The main source for this data is [the U.S. Government Department of Education
Developer portal][doe], specifically the Directory Listing for Colleges and 
University data. A copy of the data used is in the `data` directory.

This source was [found on this excellent StackOverflow question][1].

[1]: https://stackoverflow.com/questions/1937988/database-for-us-universities-and-colleges
[doe]: http://www.ed.gov/developer
