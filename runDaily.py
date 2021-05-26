import CompilePlaylists

automator = CompilePlaylists.SpotifyAutomator()

daily_mix_1_id = "37i9dQZF1E38WCLvDQLgnK"
daily_mix_2_id = "37i9dQZF1E35kfaLKg21V8"
daily_mix_3_id = "37i9dQZF1E38O7S43ixmfM"
daily_mix_4_id = "37i9dQZF1E36ZFEVc0PaI6"
daily_mix_5_id = "37i9dQZF1E39Xn4MArP6WE"
weekly_mix_id = "37i9dQZEVXcSJOMUL50oXh"

mashup_playlist_id = "2LFqITJqUlNC3PP1ke10HJ"


automator.get_songs(daily_mix_1_id)
automator.add_songs(mashup_playlist_id)
automator.clear_songs()
automator.get_songs(daily_mix_2_id)
automator.add_songs(mashup_playlist_id)
automator.clear_songs()
automator.get_songs(daily_mix_3_id)
automator.add_songs(mashup_playlist_id)
automator.clear_songs()
automator.get_songs(daily_mix_4_id)
automator.add_songs(mashup_playlist_id)
automator.clear_songs
automator.get_songs(daily_mix_5_id)
automator.add_songs(mashup_playlist_id)
automator.clear_songs