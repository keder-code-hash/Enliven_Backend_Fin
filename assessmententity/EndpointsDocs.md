`/assess`
____
**Request Body:** 
```json
{
    "type" : "upcoming/ongoing/registered"
}
```
**Response:** All upcoming/ongoing/registered Assessments

`assess/registerview`
____
**Request Body:**
```json
{
    "assessment_id" : 1
}
```
**Response:** Register Form of the Assessment with profile photo link to verify recent photo with the profile photo.

`assess/register`
____
**Request Body:**
```json
{
    "assessment_id" : 1,
    "user" : "Obj(User)"
}
```
**Response:** Successfully registered page

`/assess/create`
____
**Request Body:** 
```json
{
    "title" : "Title",
    "desc" : "Description",
    "sub" : "Subject",
    "duration" : "Time",
    "start_date" : "Starting Date time",
    "end_date" : "Ending Date time"
}
```
**Response:** Successfully created and page show for adding questions,marks,status. 