import CompilePlaylists

weekly_mix_id = "37i9dQZEVXcSJOMUL50oXh"
mashup_playlist_id = "2LFqITJqUlNC3PP1ke10HJ"

automator = CompilePlaylists.SpotifyAutomator()

automator.clear_songs()
automator.get_songs(weekly_mix_id)
automator.add_songs(mashup_playlist_id)
automator.clear_songs()