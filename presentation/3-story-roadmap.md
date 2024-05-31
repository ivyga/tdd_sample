#  Lookup Contacts

Description:  New Tool for querying an existing Contacts Database

Note: Even though we will not cover all the stories, it is nice to know the "road map" to eliminate unnecessary rework (technical debt).

## Feature 1 - Simple Lookup


<details>
<summary>Story 1 - Deploy API to validate connectivity</summary>
<b><br>AC:</b>
<br/> 
<li>New route: GET / returns 200</li>
<li>Returns <code>{ contactCount: contact-count-matching-db }</code></li>
<br/>
<b>Value:</b>

This has no "user facing value". This early release is a best practice to catch problems "early" like botched passwords, firewall issues, etc.
</details> 
<br/>
<details>
<summary>Story 2 - Deploy new route to query by last name</summary>
<b><br>AC:</b>
<br/> 
<li>New route: GET /contacts?last_name={last-name} returns 200</li>
<li>Returns <code>[{ id, firstName, lastName, email ]]</code></li>
<br/>
<b>Value:</b>
<br>
Releasing at this point has user facing value.  If the schedule was tight and there was a political/finiancial downside to not getting this out, it help to "ship" this.
</details>
<br>
<details>
<summary>Story 3 - Validate user input prior to querying</summary>
<b><br>AC:</b>
<br/> 
<li>New route: GET /contacts?last_name={invalid-input} returns 400</li>
<li>input is too short (less than 3)</li>
<li>input is malformed (characters like *, !)</li>
<li>input to short (less than 3)</li>
<br/>
<b>Value:</b>
We can not depend on a Front End UI doing this for us.  The UI does such for user experience and nefarious uses will bypass the UI.
</details>

## Feature 2 - Advanced Lookup (Future)
Story 4 - Query by partial last name
<br>
Story 5 - Query by "phonetic" last name

